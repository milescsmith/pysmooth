from .__main__ import smooth
from rich.console import Console

console = Console()

res = smooth(x=[4,5,3,8,4,4,7,8,2,8,2,9,1,6], kind="3RS3R", twiceit=False, endrule="Tukey")
console.print(res)