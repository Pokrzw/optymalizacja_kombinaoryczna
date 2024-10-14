import java.util.List;

public class AdjacencyMatrix {

    public static int[][] adjacencyUndirected(UndirectedGraph graph) {
        var vertices = graph.getVertices();
        var edges = graph.getEdges();

        int n = vertices.size();
        int[][] matrixBase = new int[n][n];
        for (Edge e : edges) {
            Vertex v1 = e.getA();
            Vertex v2 = e.getB();
            int v1i = vertices.indexOf(v1);
            int v2i = vertices.indexOf(v2);
            matrixBase[v1i][v2i]++;
            matrixBase[v2i][v1i]++;
        }
        return matrixBase;
    }

    public static int[][] adjacencyDirected(DirectedGraph graph) {
        var vertices = graph.getVertices();
        var edges = graph.getEdges();

        int n = vertices.size();
        int[][] matrixBase = new int[n][n];
        for (Edge e : edges) {
            Vertex v1 = e.getA();
            Vertex v2 = e.getB();
            int v1i = vertices.indexOf(v1);
            int v2i = vertices.indexOf(v2);
            if (v1.getName().equals(v2.getName())){
                matrixBase[v1i][v2i] += 2;
            } else {
                matrixBase[v1i][v2i]++;
            }
        }
        return matrixBase;
    }

    private static String printMatrixReusable(int[][] res, List<Vertex> vertices){
        StringBuilder finalMatrix = new StringBuilder("__|");
        for (Vertex v : vertices) {
            finalMatrix.append(" %s |".formatted(v));
        }
        finalMatrix.append("\n");

        int index = 0;
        for (Vertex v : vertices) {
            finalMatrix.append("%s |".formatted(vertices.get(index)));
            for (int i = 0; i < vertices.size(); i++) {
                finalMatrix.append(" %s |".formatted(res[index][i]));
            }
            finalMatrix.append("\n");
            index++;
        }
        return finalMatrix.toString();
    }

    public static String printMatrix(UndirectedGraph graph) {
        var matrix = AdjacencyMatrix.adjacencyUndirected(graph);
        return AdjacencyMatrix.printMatrixReusable(matrix, graph.getVertices());
    }

    public static String printMatrix(DirectedGraph graph) {
        var matrix = AdjacencyMatrix.adjacencyDirected(graph);
        return AdjacencyMatrix.printMatrixReusable(matrix, graph.getVertices());
    }
}