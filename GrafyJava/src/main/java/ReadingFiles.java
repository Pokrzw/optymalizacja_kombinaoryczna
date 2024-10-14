import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.*;

public class ReadingFiles {
    public static ArrayList<Edge> readEdgesFromFile(){
        ArrayList<Edge> createdEdges = new ArrayList<>();
        HashMap<String, Vertex> createdVerts = new HashMap<>();
        try {
            File myObj = new File("graph.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] newData = data.split(" ");
                Vertex a = createdVerts.computeIfAbsent(newData[0], Vertex::new);
                Vertex b = createdVerts.computeIfAbsent(newData[1], k -> new Vertex(k));
                createdEdges.add(new Edge(a,b));
            }
            myReader.close();
            return createdEdges;
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return createdEdges;
        }
    }
}
