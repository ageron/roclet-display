app [main!] { roclet: "https://github.com/ageron/roclet-display/releases/download/0.4.0/Gv78dUSQfYRU2yvV9HuS5oHYdMfik84S4sgsej6mbjLd.tar.zst" }
import roclet.Display
import roclet.Input

# Ordinary Roc uses the default; Roclet supplies interactive input values.
width_control = Input.slider({
    key: "width", label: "Width", min: 1, max: 10, step: 1, default: 3,
})
area = width_control.value * 4

main! = |_args| {
    expect width_control.value == 3
    expect area == 12
    echo!(Str.inspect(width_control.display))
    echo!(Str.inspect(Display.text("Area: ${area.to_str()}")))
    Ok({})
}
