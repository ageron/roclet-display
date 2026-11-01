app [main!] { roclet: "https://github.com/ageron/roclet-display/releases/download/0.4.0/Gv78dUSQfYRU2yvV9HuS5oHYdMfik84S4sgsej6mbjLd.tar.zst" }
import roclet.Display

# Rich values retain readable text when run with ordinary Roc.
main! = |_args| {
    greeting = Display.markdown("# Hello from Roc\nA small report with a table.")
    table = Display.table(["Item", "Count"], [["Apples", "3"], ["Pears", "2"]])
    echo!("${Str.inspect(greeting)}\n")
    echo!("${Str.inspect(table)}\n")
    Ok({})
}
