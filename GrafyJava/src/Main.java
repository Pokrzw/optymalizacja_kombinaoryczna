import java.util.function.Consumer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Vertex A = new Vertex("A");
        Vertex B = new Vertex("B");
        Vertex C = new Vertex("C");


        Consumer<UndirectedGraph> printInfo = (undirectedGraph) -> {
            System.out.println("<======================================>");
            System.out.printf("Vertices: %s%n",undirectedGraph.getVertices());
            System.out.printf("Edges: %s%n", undirectedGraph.getEdges());
            System.out.printf("Max vertex degree: %d%n", undirectedGraph.getMaxVertDeg());
//            System.out.printf("Min vertex degree: %d%n", undirectedGraph.getMinVertDeg());
            System.out.printf("Even degree vertex count: %d%n", undirectedGraph.getEvenDeg());
            System.out.println("<======================================>");
        };

        DirectedGraph graph1 = new DirectedGraph();
        graph1.addVertex(A);
        graph1.addVertex(B);
        graph1.addVertex(C);

        graph1.addEdge(new Edge(A, B));
        graph1.addEdge(new Edge(B, C));
        graph1.addEdge(new Edge(C, A));
        graph1.addEdge(new Edge(A, C));
        graph1.addEdge(new Edge(C, A));
        graph1.addEdge(new Edge(A, C));
        System.out.println(graph1.getVertices().toString());
        System.out.println(graph1.getEdges().toString());
        System.out.println(graph1.getInDeg().toString());
        System.out.println(graph1.getOutDeg().toString());
//        graph1.removeVertex(A);
        graph1.removeEdge(new Edge(B, C));
        System.out.println(graph1.getVertices().toString());
        System.out.println(graph1.getEdges().toString());
        System.out.println(graph1.getInDeg().toString());
        System.out.println(graph1.getOutDeg().toString());
        System.out.println(graph1.getInDeg(C));
//        MacierzSasiedztwa.sasiedztwo(graph1.getVertices(), graph1.getEdges());
        int [][] res = AdjacencyMatrix.adjacency(graph1.getVertices(), graph1.getEdges());
        System.out.println(AdjacencyMatrix.printMatrix(graph1.getVertices(), res));
    }
}