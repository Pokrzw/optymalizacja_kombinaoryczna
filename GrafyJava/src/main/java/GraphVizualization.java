import guru.nidi.graphviz.attribute.*;
import guru.nidi.graphviz.engine.Format;
import guru.nidi.graphviz.engine.Graphviz;
import guru.nidi.graphviz.model.Factory;
import guru.nidi.graphviz.model.Graph;
import guru.nidi.graphviz.model.Node;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;

import static guru.nidi.graphviz.attribute.Rank.RankDir.LEFT_TO_RIGHT;
import static guru.nidi.graphviz.model.Factory.*;
public class GraphVizualization {

    public static void vertexCoverUndirected(IGraph graph, Edge e, String fileName, STAGE stage) throws IOException{


        ArrayList<Node> linkedVerts = new ArrayList<>();
        switch (stage){
            case SELECT_EDGE -> linkedVerts = GraphVizualization.generateColoredNode(graph, e);
            case SELECT_ADJECTENT -> linkedVerts = GraphVizualization.colorAdjNodes(graph, e);
            case GENERATE_GRAPH -> linkedVerts = GraphVizualization.generateNodes(graph);
            case REMOVE_EDGES -> linkedVerts = GraphVizualization.removeAdjNodes(graph, e);
        }

        Graph g = graph("x")
                .graphAttr().with(Rank.dir(LEFT_TO_RIGHT))
                .graphAttr().with(GraphAttr.FORCE_LABELS_NOT)
                .linkAttr().with("class", "link-class")
                .with(
                        linkedVerts
                );


        Graphviz.fromGraph(g).height(300).render(Format.SVG).toFile(new File(String.format("vertexCov/%s.svg", fileName)));
    }
    private static ArrayList<Node> removeAdjNodes(IGraph graph, Edge edge){
        var edges = graph.getEdges();
        ArrayList<Node> nodes = new ArrayList<>();
        int i=1;
        HashSet<Vertex> unvisited = new HashSet<>(graph.getVertices());
        for (Edge e: edges){
            unvisited.remove(e.getA());
            unvisited.remove(e.getB());
            String n1Name = e.getA().getName();
            String n2Name = e.getB().getName();
            ArrayList<String> names = new ArrayList<>();
            names.add(n1Name);
            names.add(n2Name);
            Node n1 = Factory.node(n1Name);
            Node n2 = Factory.node(n2Name);

            if (!(names.contains(edge.getA().getName()) || names.contains(edge.getB().getName()))){
                Node l = n1.link(to(n2).with("id", String.valueOf(i)));
                nodes.add(l);
            }
            i++;
        }
        for(var vertex : unvisited){
            Node n = Factory.node(vertex.getName());
            nodes.add(n);
        }
        return nodes;
    }
    private static ArrayList<Node> colorAdjNodes(IGraph graph, Edge edge){
        var edges = graph.getEdges();
        ArrayList<Node> nodes = new ArrayList<>();
        int i=1;
        HashSet<Vertex> unvisited = new HashSet<>(graph.getVertices());
        for (Edge e: edges){
            unvisited.remove(e.getA());
            unvisited.remove(e.getB());
            String n1Name = e.getA().getName();
            String n2Name = e.getB().getName();
            ArrayList<String> names = new ArrayList<>();
            names.add(n1Name);
            names.add(n2Name);
            Node n1 = Factory.node(n1Name);
            Node n2 = Factory.node(n2Name);
            if (e.getA().equals(edge.getA()) && e.getB().equals(edge.getB())){
                Node l = n1.link(to(n2).with("id", String.valueOf(i)).with(Color.RED));
                nodes.add(l);
            } else if(names.contains(edge.getA().getName()) || names.contains(edge.getB().getName())){
                Node l = n1.link(to(n2).with("id", String.valueOf(i)).with(Color.CYAN1));
                nodes.add(l);
            }
            else{
                Node l = n1.link(to(n2).with("id", String.valueOf(i)));
                nodes.add(l);
            }

            i++;
        }
        for(var vertex : unvisited){
            Node n = Factory.node(vertex.getName());
            nodes.add(n);
        }
        return nodes;
    }

    private static ArrayList<Node> generateColoredNode(IGraph graph, Edge edge){
        var edges = graph.getEdges();
        ArrayList<Node> nodes = new ArrayList<>();
        int i=1;
        HashSet<Vertex> unvisited = new HashSet<>(graph.getVertices());
        for (Edge e: edges){
            unvisited.remove(e.getA());
            unvisited.remove(e.getB());
            String n1Name = e.getA().getName();
            String n2Name = e.getB().getName();
            Node n1 = Factory.node(n1Name);
            Node n2 = Factory.node(n2Name);
            if (e.getA().equals(edge.getA()) && e.getB().equals(edge.getB())){
                Node l = n1.link(to(n2).with("id", String.valueOf(i)).with(Color.RED));
                nodes.add(l);
            }
            else{
                Node l = n1.link(to(n2).with("id", String.valueOf(i)));
                nodes.add(l);
            }

            i++;
        }
        for(var vertex : unvisited){
            Node n = Factory.node(vertex.getName());
            nodes.add(n);
        }
        return nodes;
    }
    private static ArrayList<Node> generateNodes(IGraph graph){
        var edges = graph.getEdges();
        ArrayList<Node> nodes = new ArrayList<>();
        int i=1;
        HashSet<Vertex> unvisited = new HashSet<>(graph.getVertices());
        for (Edge e: edges){
            unvisited.remove(e.getA());
            unvisited.remove(e.getB());
            String n1Name = e.getA().getName();
            String n2Name = e.getB().getName();
            Node n1 = Factory.node(n1Name);
            Node n2 = Factory.node(n2Name);
            Node l = n1.link(to(n2).with("id", String.valueOf(i)));
            i++;
            nodes.add(l);
        }
        for(var vertex : unvisited){
            Node n = Factory.node(vertex.getName());
            nodes.add(n);
        }
        return nodes;
    }
    public static void generateUndirectedGraph(UndirectedGraph graph) throws IOException {
        ArrayList<Node> linkedVerts = GraphVizualization.generateNodes(graph);
        Graph g = graph("x")
                .graphAttr().with(Rank.dir(LEFT_TO_RIGHT))
                .graphAttr().with(GraphAttr.FORCE_LABELS_NOT)
                .linkAttr().with("class", "link-class")
                .with(
                    linkedVerts
                );

        Graphviz.fromGraph(g).height(300).render(Format.SVG).toFile(new File("example/undirected.svg"));
    }
    public static void generateDirectedGraph(DirectedGraph graph) throws IOException {
        ArrayList<Node> linkedVerts = GraphVizualization.generateNodes(graph);
        Graph g = graph("x").directed()
                .graphAttr().with(Rank.dir(LEFT_TO_RIGHT))
                .graphAttr().with(GraphAttr.FORCE_LABELS_NOT)
                .linkAttr().with("class", "link-class")
                .with(
                        linkedVerts
                );

        Graphviz.fromGraph(g).height(300).render(Format.SVG).toFile(new File("example/directed.svg"));
    }
}
