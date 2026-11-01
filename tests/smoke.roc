app [main!] { roclet: "../package/main.roc" }
import roclet.Display
import roclet.Input

main! = |_args| {
    control = Input.slider({ key: "width", label: "Width", min: 1, max: 10, step: 1, default: 3 })
    custom = Input.custom({ key: "custom", label: "Custom", min: 0, max: 10, default: 2, html: "<input>" })
    expect control.value == 3
    expect custom.value == 2
    echo!(Str.inspect(Display.text("hello")))
    echo!(Str.inspect(Display.markdown("# Hello")))
    echo!(Str.inspect(Display.table(["Name"], [["Roc"]])))
    echo!(Str.inspect(Display.image("Image", "image/png", "")))
    echo!(Str.inspect(Display.html("HTML", "<p>Hello</p>")))
    echo!(Str.inspect(Display.svg("SVG", "<svg></svg>")))
    echo!(Str.inspect(Display.widget("Widget", "<button>Hello</button>")))
    echo!(Str.inspect(Display.plotly("Chart", "{\"data\":[],\"layout\":{}}")))
    echo!(Str.inspect(control.display))
    echo!(Str.inspect(custom.display))
    Ok({})
}
