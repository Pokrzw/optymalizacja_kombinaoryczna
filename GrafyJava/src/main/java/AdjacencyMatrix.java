import java.util.ArrayList;
import java.util.Arrays;

public class AdjacencyMatrix {

    public static int[][] adjacencyUndirected(ArrayList<Vertex> vertices, ArrayList<Edge> edges) {
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

    public static int[][] adjacencyDirected(ArrayList<Vertex> vertices, ArrayList<Edge> edges) {
        int n = vertices.size();
        int[][] matrixBase = new int[n][n];
        for (Edge e : edges) {
            System.out.println(e);
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

    public static String printMatrix(ArrayList<Vertex> vertices, int[][] res) {
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
}