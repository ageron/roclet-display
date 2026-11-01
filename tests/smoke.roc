app [main!] { roclet: "../package/main.roc" }
import roclet.Display
import roclet.Input

main! = |_args| {
    control = Input.slider({ key: "width", label: "Width", min: 1, max: 10, step: 1, default: 3 })
    custom = Input.custom({ key: "custom", label: "Custom", min: 0, max: 10, default: 2, html: "<input>" })
    expect control.value == 3
    expect custom.value == 2
    echo!("${Str.inspect(Display.text("hello"))}\n")
    echo!("${Str.inspect(Display.markdown("# Hello"))}\n")
    echo!("${Str.inspect(Display.table(["Name"], [["Roc"]]))}\n")
    echo!("${Str.inspect(Display.image("Image", "image/png", ""))}\n")
    echo!("${Str.inspect(Display.html("HTML", "<p>Hello</p>"))}\n")
    echo!("${Str.inspect(Display.svg("SVG", "<svg></svg>"))}\n")
    echo!("${Str.inspect(Display.widget("Widget", "<button>Hello</button>"))}\n")
    echo!("${Str.inspect(Display.plotly("Chart", "{\"data\":[],\"layout\":{}}"))}\n")
    echo!("${Str.inspect(control.display)}\n")
    echo!("${Str.inspect(custom.display)}\n")
    Ok({})
}
