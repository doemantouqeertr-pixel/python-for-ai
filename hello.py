
#REVISION FOR TOPICS I HAVE LEARNT IN PYTHON
 

#printing single line comment

print("Hello World")
print(' hello eman')
#printing double line comment

print('''I rebel therefore I exist,
but right now 
i am learning python
from scratch and this is my multiline comment ml''')




#   pip packages [rich]

from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Python Practice Log")
table.add_column("Day", style="cyan")
table.add_column("Topic", style="magenta")
table.add_column("Status", style="green")

table.add_row("1", "Variables & Loops", "✅ Done")
table.add_row("2", "Functions", "🔄 In Progress")

console.print(table)



#pip packages [pyfiglet]

import pyfiglet
print(pyfiglet.figlet_format("DOTREMANT"))





# pip packages [requests]

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

