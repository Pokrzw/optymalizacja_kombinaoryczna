import guru.nidi.graphviz.attribute.*;
import guru.nidi.graphviz.engine.Format;
import guru.nidi.graphviz.engine.Graphviz;
import guru.nidi.graphviz.model.Factory;
import guru.nidi.graphviz.model.Graph;
import guru.nidi.graphviz.model.Node;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import static guru.nidi.graphviz.attribute.Attributes.attr;
import static guru.nidi.graphviz.attribute.Rank.RankDir.LEFT_TO_RIGHT;
import static guru.nidi.graphviz.model.Factory.*;
public class GraphVizualization {

    private static ArrayList<Node> generateNodes(ArrayList<Edge> edges){
        ArrayList<Node> nodes = new ArrayList<>();
        for (Edge e: edges){
            Node n = Factory.node(e.getA().getName()).link(Factory.node(e.getB().getName()));
            nodes.add(n);
        }
        return nodes;
    }
    public static void generateUndirectedGraph(UndirectedGraph graph) throws IOException {
        ArrayList<Node> linkedVerts = GraphVizualization.generateNodes(graph.getEdges());
        Graph g = graph("x").graphAttr().with(Rank.dir(LEFT_TO_RIGHT))
                .linkAttr().with("class", "link-class")
                .with(
                    linkedVerts
                );

        Graphviz.fromGraph(g).height(300).render(Format.PNG).toFile(new File("example/undirected.png"));
    }
    public static void generateDirectedGraph(DirectedGraph graph) throws IOException {
        ArrayList<Node> linkedVerts = GraphVizualization.generateNodes(graph.getEdges());
        Graph g = graph("x").directed().graphAttr().with(Rank.dir(LEFT_TO_RIGHT))
                .linkAttr().with("class", "link-class")
                .with(
                        linkedVerts
                );

        Graphviz.fromGraph(g).height(300).render(Format.PNG).toFile(new File("example/directed.png"));
    }
}
