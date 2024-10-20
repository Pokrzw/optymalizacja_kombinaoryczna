import java.util.ArrayList;
import java.util.Random;

public class VertexCoverApprox {
    static public int VertexCover(IGraph graph) {
        ArrayList<Edge> edges = graph.getEdges();
        System.out.println("Krawedzie grafu: " + edges);
        ArrayList<Vertex> vprime = new ArrayList<>();
        System.out.println("Aktualne wierzchołki w zbiorze V': " + vprime);

        while (edges.size() > 0) {
            Edge randomisedEdge = genetrateRandomEdge(edges);
            System.out.println("Wylosowana krawedz: " + randomisedEdge);
            edges.remove(randomisedEdge);
            System.out.println("Usunieto wylosowana krawedz: " + edges);

            ArrayList<Edge> edgesCopy = edges;

            Vertex vertA = randomisedEdge.getA();
            Vertex vertB = randomisedEdge.getB();
            vprime.add(vertA);
            vprime.add(vertB);
            System.out.println("Zbior krawedzi: " + vprime);

            for (Edge e : edgesCopy){
                if (e.getA().equals(vertA) || e.getB().equals(vertB)){
                    System.out.println("Krawedz " + e + " ma wspolny wierzcholek" + vertA + " lub " + vertB + " z krawedzia " + randomisedEdge);
                    edges.remove(e);
                }
            }

            System.out.println("Aktualne krawedzie: " + edges);
        }
        return vprime.size();
    }

    static private Edge genetrateRandomEdge(ArrayList<Edge> edges) {
        Random rand = new Random();
        int maxIndex = edges.size()-1;
        int randomIndex = rand.nextInt(maxIndex);
        return edges.get(randomIndex);
    }
}
