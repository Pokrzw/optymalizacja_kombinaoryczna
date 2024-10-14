import java.util.ArrayList;

public interface IGraph {
    ArrayList<Vertex> getVertices();
    ArrayList<Edge> getEdges();
    IGraph addVertex(Vertex a);
    IGraph addEdge(Edge a);
    IGraph removeVertex(Vertex a);
    IGraph removeEdge(Edge a);
}
