import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<Edge> edges = ReadingFiles.readEdgesFromFile();
        DirectedGraph diGraph = new DirectedGraph(edges);
        UndirectedGraph unGraph = new UndirectedGraph(edges);

        var graph = diGraph;
        var one = graph.getVertices().stream().filter(vertex -> vertex.getName().equals("a")).findFirst().get();
        var three = graph.getVertices().stream().filter(vertex -> vertex.getName().equals("b")).findFirst().get();
        var two = graph.getVertices().stream().filter(vertex -> vertex.getName().equals("c")).findFirst().get();

//        graph.removeEdge(new Edge(one, one));
//        graph.removeVertex(two);
//        Vertex P = new Vertex("P");
//        graph.addVertex(P);
//        graph.addEdge(new Edge(P, P));
//        System.out.println(graph.getVertices());
//        System.out.println(graph.getEdges());
//        System.out.println(graph.getMappings());
        System.out.println(graph.getInDeg().toString());
        System.out.println(graph.getOutDeg().toString());
        var adjacency = AdjacencyMatrix.printMatrix(diGraph);
        System.out.println("Directed graph adjacency matrix");
        System.out.println(adjacency);
        adjacency = AdjacencyMatrix.printMatrix(unGraph);
        System.out.println("Undirected graph adjacency matrix");
        System.out.println(adjacency);
        GraphVizualization.generateUndirectedGraph(unGraph);
        GraphVizualization.generateDirectedGraph(diGraph);
    }
}