pip install textstat

# English
import textstat
textstat.set_lang("en")

text = """
Data science is the main focus of most sciences and studies right now, 
it needs a lot of things like AI, programming, statistics, 
business understanding, effective presentation skills and much more. 
That's why it's not easy to understand or study. But we can do it, we are doing it.
Data science has become the standard solving problem framework for academia and 
the industry and it's going to be like that for a while. But we need to remember 
where we are coming from, who we are and where we are going.
"""

# Run all at once
import inspect
funcs = ["textstat." + inspect.getmembers(textstat, predicate=inspect.ismethod)[i][0] for i in range(1,28)]

for elem in funcs:
    method = eval(elem)
    textstat.set_lang("en")
    print(elem.split(".")[1])
    print(method(text))
    print(" ")