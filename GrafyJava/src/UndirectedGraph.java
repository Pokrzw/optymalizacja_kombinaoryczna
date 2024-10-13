import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class UndirectedGraph {
    private ArrayList<Vertex> vertices;
    private ArrayList<Edge> edges;
    private HashMap<Vertex, ArrayList<Vertex>> mappings;


    public UndirectedGraph() {
        this.vertices = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.mappings = new HashMap<>();
    }

    public ArrayList<Vertex> getVertices() {
        return vertices;
    }
    public ArrayList<Edge> getEdges() {
        return edges;
    }
    public HashMap<Vertex, ArrayList<Vertex>> getMappings() {
        return mappings;
    }


    public void addVertex(Vertex a){
        if(!vertices.contains(a)){
            vertices.add(a);
        }
    }
    private void dissolve(Vertex a){
        edges.removeIf(e -> e.getConnection().contains(a));
    }
    private void addMappings(Vertex a, Vertex b){
        if(!mappings.containsKey(a)){
            mappings.put(a, new ArrayList<>());
        }
        if(!mappings.containsKey(b)){
            mappings.put(b, new ArrayList<>());
        }
        ArrayList<Vertex> newAList = mappings.get(a);
        newAList.add(b);

        ArrayList<Vertex> newBList = mappings.get(b);
        newBList.add(a);

        mappings.put(a, newAList);
        mappings.put(b, newBList);
    }

    private void removeMappings(Vertex a){
        HashMap<Vertex, ArrayList<Vertex>> newMappings = new HashMap<>(mappings);

        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  mappings.entrySet()){
            if(currentVertex.getKey()==a){
                newMappings.remove(a);
            }
            if (currentVertex.getValue().contains(a)){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(a);
                newMappings.put(currentVertex.getKey(), currValues);
            }
        }
        mappings = newMappings;
    }

    public void deleteVertex(Vertex a){
        //1. DISSOLVOWANIE EDGES ZAWIERAJACYCH VERTEX
        dissolve(a);
       //2. USUWANIE ZALEZNOSCI
        removeMappings(a);
      //3. WYWALANIE VERTEX Z LISTY VERTICES
        vertices.remove(a);
    }

    public void addEdge(Edge e){
        //1. SPRAWDZIC CZY ISTNIEJA ODPOWIEDNIE WIERZCHOLKI
        if(!vertices.contains(e.getA()) || !vertices.contains(e.getB())) {
            return;
        }
        //2. SPRAWDZIC CZY NIE POWTARZAJA SIE KRAWEDZIE
        ArrayList<Vertex> checkedEdge = e.getConnection();
        for(Edge f: edges){
            ArrayList<Vertex> currentEdge = f.getConnection();
            if(checkedEdge.equals(currentEdge) || checkedEdge.reversed().equals(currentEdge)){
                return;
            }
        }
        //3. DODAC DO LISTY
        edges.add(e);
        //4. DODAC ZALEZNOSCI
        addMappings(e.getA(), e.getB());
    }

    public void removeEdge(Edge e){
        //1. SPRAWDZIC CZY ISTNIEJA ODPOWIEDNIE WIERZCHOLKI
        if(!vertices.contains(e.getA()) || !vertices.contains(e.getB())) {
            return;
        }

        //2. SPRAWDZIC CZY ISTNIEJE KRAWEDZ
        ArrayList<Vertex> checkedEdge = e.getConnection();
        for(Edge f: edges){
            ArrayList<Vertex> currentEdge = f.getConnection();
            if(checkedEdge.equals(currentEdge) || checkedEdge.reversed().equals(currentEdge)){
                e = f;
            }
        }
        edges.remove(e);


//ZROBIC MAPPINGI DLA USUWANIA EDGES -> BEZ USUWANIA KOMPLETNEGO KLUCZA
//        removeMappingsFor2(e.getA(), e.getB());
//        removeMappings(e.getA());
//        removeMappings(e.getB());
        removeEdgeMapping(e);

    }
    public void removeEdgeMapping(Edge e){
        HashMap<Vertex, ArrayList<Vertex>> newMappings = new HashMap<>(mappings);
        Vertex v1 = e.getA();
        Vertex v2 = e.getB();

        for (Map.Entry<Vertex, ArrayList<Vertex>> currentVertex:  mappings.entrySet()){
            if (currentVertex.getKey()== v2){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(v1);
                newMappings.put(currentVertex.getKey(), currValues);
            }
            if (currentVertex.getKey()== v1){
                ArrayList<Vertex> currValues = currentVertex.getValue();
                currValues.remove(v2);
                newMappings.put(currentVertex.getKey(), currValues);
            }
        }
        mappings = newMappings;
    }

    public int getVertexDeg(Vertex v){
        if (!mappings.containsKey(v)){
            return -1;
        }
        return mappings.get(v).size();
    }

    public int getMaxVertDeg(){
        int maxVal = 0;
        for(Map.Entry<Vertex, ArrayList<Vertex>> currentVertex: mappings.entrySet()){
            if(currentVertex.getValue().size()>maxVal){
                maxVal = currentVertex.getValue().size();
            }
        }
        return maxVal;
    }

    public int getMinVertDeg(){
        if (mappings.isEmpty()){
            return -1;
        }
        int minVal = mappings.entrySet().iterator().next().getValue().size();
        for(Map.Entry<Vertex, ArrayList<Vertex>> currentVertex: mappings.entrySet()){
            if(currentVertex.getValue().size()<minVal){
                minVal = currentVertex.getValue().size();
            }
        }
        return minVal;
    }

    public int getEvenDeg(){
        int evenDegs = 0;
        for(Map.Entry<Vertex, ArrayList<Vertex>> currentVertex: mappings.entrySet()){
            if(currentVertex.getValue().size()%2==0){
                evenDegs++;
            }
        }
        return evenDegs;
    }

    public int getUnevenDeg(){
        int unevenDegs = 0;
        for(Map.Entry<Vertex, ArrayList<Vertex>> currentVertex: mappings.entrySet()){
            if(currentVertex.getValue().size()%2!=0){
                unevenDegs++;
            }
        }
        return unevenDegs;
    }

    public ArrayList<Integer> sortedDegs(){
        ArrayList<Integer> unsortedList = new ArrayList<>();
        for(Map.Entry<Vertex, ArrayList<Vertex>> currentVertex: mappings.entrySet()){
            unsortedList.add(currentVertex.getValue().size());
        }
        Collections.sort(unsortedList, Collections.reverseOrder());
        return unsortedList;
    }
}

