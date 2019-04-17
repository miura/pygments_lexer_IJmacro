# Pygment Command example

```
pygmentize -l ./imagejmacro.py:ImageJMacroLexer  -x -O full,style=tango,linenos=1 -o testout.html testcode.ijm
```



## Compiling

To complie a latex code with pygment lexer for ImageJ macro, do not forget the option `-shell-escape`. 

```
pdflatex -shell-escape example.tex
```

