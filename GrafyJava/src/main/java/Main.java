import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<Edge> edges = ReadingFiles.readEdgesFromFile();
        UndirectedGraph graph = new UndirectedGraph(edges);
        GraphVizualization.generateUndirectedGraph(graph);
        DirectedGraph graph1 = new DirectedGraph(edges);
        GraphVizualization.generateDirectedGraph(graph1);
        var vert = graph1.getVertices().stream().filter(vertex -> vertex.getName().equals("6")).findFirst();
        System.out.println(
            AdjacencyMatrix.printMatrix(graph.getVertices(), AdjacencyMatrix.adjacencyDirected(graph.getVertices(), graph.getEdges()))
            );
    }
}