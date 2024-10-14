import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DirectedGraph implements IGraph {
    private ArrayList<Vertex> vertices;
    private ArrayList<Edge> edges;
    //Stopnie wchodzace
    private HashMap<Vertex, ArrayList<Vertex>> inDeg;
    //Stopnie wychodzace
    private HashMap<Vertex, ArrayList<Vertex>> outDeg;

    public DirectedGraph(){
        this.vertices = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.inDeg = new HashMap<>();
        this.outDeg = new HashMap<>();
    }

    public DirectedGraph(List<Edge> edges){
        this.vertices = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.inDeg = new HashMap<>();
        this.outDeg = new HashMap<>();

        for (Edge e: edges){
            addVertex(e.getA()).addVertex(e.getB()).addEdge(e);
        }
    }


    public ArrayList<Vertex> getVertices() {return vertices;}
    public ArrayList<Edge> getEdges() {return edges;}
    public HashMap<Vertex, ArrayList<Vertex>> getInDeg() {return inDeg;}
    public HashMap<Vertex, ArrayList<Vertex>> getOutDeg() {return outDeg;}

    public DirectedGraph addVertex(Vertex a){
        if(!vertices.contains(a)){
            vertices.add(a);
        }
        return this;
    }

    public DirectedGraph addEdge(Edge e){
        if(!vertices.contains(e.getA()) || !vertices.contains(e.getB())) {
            return this;
        }
        ArrayList<Vertex> checkedEdge = e.getConnection();
        for(Edge f: edges){
            ArrayList<Vertex> currentEdge = f.getConnection();
            if(checkedEdge.equals(currentEdge)){
                return this;
            }
        }
        edges.add(e);

        addMappings(e.getA(), e.getB(), outDeg);
        addMappings(e.getB(), e.getA(), inDeg);
        return this;
    }

    private void addMappings(Vertex a, Vertex b, HashMap<Vertex, ArrayList<Vertex>> mapList){
        if(!mapList.containsKey(a)){
            mapList.put(a, new ArrayList<>());
        }
        ArrayList<Vertex> newAList = mapList.get(a);
        newAList.add(b);
        mapList.put(a, newAList);
    }

    public DirectedGraph removeVertex(Vertex a){
        vertices.remove(a);
        ArrayList<Edge> newEdges = new ArrayList<>(edges);
        for(Edge e: edges){
            if(e.getConnection().contains(a)){
                newEdges.remove(e);
            }
        }
        edges = newEdges;
        //3. Usun krawedz z wszystkich mappingow
        HashMap<Vertex, ArrayList<Vertex>> newOutDeg = new HashMap<>(outDeg);
        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  outDeg.entrySet()){
            if (currentVertex.getKey().equals(a)){
                newOutDeg.remove(a);
            }

            if(currentVertex.getValue().contains(a)){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(a);
                newOutDeg.put(currentVertex.getKey(), currValues);
            }
        }

        outDeg = newOutDeg;

        HashMap<Vertex, ArrayList<Vertex>> newInDeg = new HashMap<>(inDeg);
        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  inDeg.entrySet()){
            if (currentVertex.getKey().equals(a)){
                newInDeg.remove(a);
            }

            if(currentVertex.getValue().contains(a)){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(a);
                newInDeg.put(currentVertex.getKey(), currValues);
            }
        }
        inDeg = newInDeg;

        return this;
    }

    public DirectedGraph removeEdge(Edge e){
        //1. SPRAWDZIC CZY ISTNIEJA ODPOWIEDNIE WIERZCHOLKI
        if(!vertices.contains(e.getA()) || !vertices.contains(e.getB())) {
            return this;
        }
        //1. Usun z edges
        ArrayList<Vertex> checkedEdge = e.getConnection();
        for(Edge f: edges){
            ArrayList<Vertex> currentEdge = f.getConnection();
            if(checkedEdge.equals(currentEdge) || checkedEdge.reversed().equals(currentEdge)){
                e = f;
            }
        }
        edges.remove(e);

        Vertex a = e.getA();
        Vertex b = e.getB();
        //2. Usunac mappingi indDeg in outDeg

        HashMap<Vertex, ArrayList<Vertex>> newInDeg = new HashMap<>(inDeg);
        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  inDeg.entrySet()){
            if(currentVertex.getKey().equals(b) && currentVertex.getValue().contains(a)){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(a);
                newInDeg.put(currentVertex.getKey(), currValues);
            }
        }

        inDeg = newInDeg;

        HashMap<Vertex, ArrayList<Vertex>> newOutDeg = new HashMap<>(outDeg);
        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  outDeg.entrySet()){
            if(currentVertex.getKey().equals(a) && currentVertex.getValue().contains(b)){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(b);
                newOutDeg.put(currentVertex.getKey(), currValues);
            }
        }

        outDeg = newOutDeg;
        return this;
    }

    public int getOutDeg(Vertex a){
        return outDeg.get(a).size();
    }

    public int getInDeg(Vertex a){
        return inDeg.get(a).size();
    }
}
