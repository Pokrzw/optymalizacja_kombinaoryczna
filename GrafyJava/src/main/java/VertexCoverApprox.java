import java.io.IOException;
import java.util.*;

public class VertexCoverApprox {
    static public int VertexCover(IGraph graph) throws IOException {
        int stageCount = 0;
//        IGraph graphCopy = graph;
        ArrayList<Edge> edges = graph.getEdges();
//        System.out.println("Krawedzie grafu: " + edges);
        ArrayList<Vertex> vprime = new ArrayList<>();
//        System.out.println("Aktualne wierzchołki w zbiorze V': " + vprime);
        GraphVizualization.vertexCoverUndirected(graph, graph.getEdges().get(0), String.format("0BegGraph"), STAGE.GENERATE_GRAPH);

        while (edges.size() > 0) {
            //poczatek przechodzenia przez usuwanie i losowanie krawedzi
            Edge randomisedEdge = genetrateRandomEdge(edges);


//            System.out.println("Wylosowana krawedz: " + randomisedEdge);

            GraphVizualization.vertexCoverUndirected(graph, randomisedEdge, String.format("%sEdge", stageCount), STAGE.SELECT_EDGE);
            GraphVizualization.vertexCoverUndirected(graph, randomisedEdge, String.format("%sEdgeAdj", stageCount), STAGE.SELECT_ADJECTENT);
            GraphVizualization.vertexCoverUndirected(graph, randomisedEdge, String.format("%sRemEdge", stageCount), STAGE.REMOVE_EDGES);

            edges.remove(randomisedEdge);
            graph.removeEdge(randomisedEdge);
//            System.out.println("Usunieto wylosowana krawedz: " + edges);

            ArrayList<Edge> edgesToRemove = new ArrayList<>();

            Vertex vertA = randomisedEdge.getA();
            Vertex vertB = randomisedEdge.getB();
            vprime.add(vertA);
            vprime.add(vertB);
            System.out.println("Zbior wierzcholkow: " + vprime);

//            for (Edge e : edges){
//                if (e.getA().equals(vertA) || e.getB().equals(vertB) || e.getA().equals(vertB) || e.getB().equals(vertA)){
//                    System.out.println("Krawedz " + e + " ma wspolny wierzcholek" + vertA + " lub " + vertB + " z krawedzia " + randomisedEdge);
//                    edges.remove(e);
//                }
//            }

            for (int i=0;i<edges.size();i++) {

                if (edges.get(i).getA().equals(vertA) || edges.get(i).getB().equals(vertB) || edges.get(i).getA().equals(vertB) || edges.get(i).getB().equals(vertA)) {
                    System.out.println("Krawedz " + edges.get(i) + " ma wspolny wierzcholek " + vertA + " lub " + vertB + " z krawedzia " + randomisedEdge);
                    edgesToRemove.add(edges.get(i));

                }
                else {
                    System.out.println("Krawedz "+edges.get(i) + " nie ma wspolnych krawedzi z "+ randomisedEdge);
                }
            }
            for (Edge e: edgesToRemove){
                edges.remove(e);
                graph.removeEdge(e);
            }
            List<Vertex> vertsInEdg = graph.getEdges()
                    .stream()
                    .map(e -> {
                        List<Vertex> verts = new ArrayList<>();
                        verts.add(e.getA());
                        verts.add(e.getB());
                        return verts;
                    })
                    .flatMap(Collection::stream)
                    .toList()
                    ;

            Set<Vertex> vertsSet = Set.copyOf(vertsInEdg);
            ArrayList<Vertex> vertsInGraph = graph.getVertices();
            ArrayList<Vertex> vertsToRemove = new ArrayList<>();
            for (Vertex v: vertsInGraph){
                if(!vertsSet.contains(v)){
                    vertsToRemove.add(v);
                }
            }

            for(Vertex v: vertsToRemove){
                graph.removeVertex(v);

            }
            System.out.println("Aktualne krawedzie (po usunieciu kopii): " + edges);

            stageCount++;
        }

        return vprime.size();
    }

    static private Edge genetrateRandomEdge(ArrayList<Edge> edges) {
        Random rand = new Random();

        int maxIndex = edges.size()-1;
        int randomIndex = (maxIndex>0) ? rand.nextInt(maxIndex) : 0;
        System.out.println("Wygenerowany indeks: " + randomIndex);
        return edges.get(randomIndex);
    }
}
