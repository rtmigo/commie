from pathlib import Path

import commie

if __name__ == "__main__":

	# in this example we'll parse a Go source file
	file = Path(__file__).parent / "data" / "multiply.go"

	source_code:str = file.read_text()

	for comment in commie.iter_comments(source_code, filename=file.name):
		# comment code: "/* sample */"
		print("Comment code:", comment.code)
		print("Comment code location:", comment.code_span.start, comment.code_span.end)

		# comment text: " sample "
		print("Comment inner text:", comment.text)
		print("Comment text location:", comment.text_span.start, comment.text_span.end)
