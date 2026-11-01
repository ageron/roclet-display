app [main!] { roclet: "../package/main.roc" }
import roclet.Display

# Plotly JSON needs data and layout. No Plume dependency is needed for this example.
figure =
    \\{"data":[{"type":"bar","x":["Apples","Pears"],"y":[3,2]}],"layout":{"title":{"text":"Fruit counts"}}}

main! = |_args| {
    chart = Display.plotly("Fruit counts: 3 apples and 2 pears.", figure)
    echo!(Str.inspect(chart))
    Ok({})
}
