import java.util.ArrayList;

public class Edge{
    private Vertex a;
    private Vertex b;
    private ArrayList<Vertex> connection = new ArrayList<>();

    public Edge(Vertex a, Vertex b) {
        this.a = a;
        this.b = b;
        this.connection.add(a);
        this.connection.add(b);
    }
    public Vertex getA() {
        return a;
    }

    public Vertex getB() {
        return b;
    }

    public ArrayList<Vertex> getConnection(){
        return connection;
    }
    @Override
    public String toString() {
        String edgeString = "[%s, %s]";
        return String.format(edgeString, a.getName(), b.getName());
    }
}