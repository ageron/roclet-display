app [main!] { roclet: "../package/main.roc" }
import roclet.Display

# Rich values retain readable text when run with ordinary Roc.
main! = |_args| {
    greeting = Display.markdown("# Hello from Roc\nA small report with a table.")
    table = Display.table(["Item", "Count"], [["Apples", "3"], ["Pears", "2"]])
    echo!(Str.inspect(greeting))
    echo!(Str.inspect(table))
    Ok({})
}
