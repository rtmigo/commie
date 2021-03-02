from pathlib import Path

import commie

# in this example we'll parse a Go source file
file = Path(__file__).parent / "data" / "multiply.go"

sourceCode = file.read_text()

for comment in commie.iter_comments(file.read_text(), file.name):
	# comment code: "/* sample */"
	print("Comment code:", comment.code)
	print("Comment code location:", comment.code_span.start, comment.code_span.end)

	# comment text: " sample "
	print("Comment inner text:", comment.text)
	print("Comment text location:", comment.text_span.start, comment.text_span.end)
