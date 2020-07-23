# Stonecharioteer.com Blog

This is the jeykyll source code for my blog. I use [YAMT](https://github.com/PandaSekh/Jekyll-YAMT)
for the layout and the themes.


## Snippet for Title Block for markdown files
```json
{
	// Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"titleblock": {
		"prefix": "title",
		"body": [
			"---",
			"title: $1",
			"layout: post",
			"categories: [$2]",
			"image: /assets/images/posts/$3",
			"description: \"$4\"",
			"customexcerpt: \"$5\"",
			"---"
			
		]
	}
}
```