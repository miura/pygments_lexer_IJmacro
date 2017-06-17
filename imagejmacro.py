# -*- coding: utf-8 -*-
"""
    pygments.lexers.imagej_macro
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for ImageJ Macro.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, default, using, \
    this, words, combined
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Other
from pygments.util import get_bool_opt, iteritems
import pygments.unistring as uni

__all__ = ['ImageJMacroLexer']


class ImageJMacroLexer(RegexLexer):
#class CustomLexer(RegexLexer):
    
    """
    Pygments Lexer for ImageJ Macro files (.ijm).
    See https://imagej.nih.gov/ij/developer/macro/functions.html.
    As of 2017/05/01 

    .. versionadded:: 1.0
    """

    name = 'ImageJ_Macro'
    aliases = ['ijmacro']
    filenames = ['*.ijm']
    mimetypes = ['text/ijm']

    flags = re.DOTALL | re.UNICODE | re.IGNORECASE | re.MULTILINE

    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'<!--', Comment),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gimuy]+\b|\B)', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')
        ],
        'badregex': [
            (r'\n', Text, '#pop')
        ],
        'root': [
            (r'\A#! ?/.*?\n', Comment.Hashbang),  # recognized by node.js
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'(\.\d+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?', Number.Float),
            (r'0[bB][01]+', Number.Bin),
            (r'0[oO][0-7]+', Number.Oct),
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'\.\.\.|=>', Punctuation),
            (r'\+\+|--|~|&&|\?|:|\|\||\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|[-<>+*%&|^/])=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(for|in|while|do|return|if|else)\b', Keyword, 'slashstartsregex'),
            (r'(var|macro|function)\b', Keyword.Declaration, 'slashstartsregex'),
            (r'(true|false|NaN|PI)\b', Keyword.Constant),
            (r'(Array.concat|Array.copy|Array.fill|Array.findMaxima|'
                r'Array.findMinima|Array.fourier|Array.getSequence|'
                r'Array.getStatistics|Array.getVertexAngles|Array.print|'
                r'Array.rankPositions|Array.resample|Array.reverse|'
                r'Array.rotate|Array.show|Array.slice|Array.sort|Array.trim|'
                r'Dialog.addCheckbox|Dialog.addCheckboxGroup|Dialog.addChoice|'
                r'Dialog.addHelp|Dialog.addMessage|Dialog.addNumber|'
                r'Dialog.addRadioButtonGroup|Dialog.addSlider|Dialog.addString|'
                r'Dialog.create|Dialog.getCheckbox|Dialog.getChoice|Dialog.getNumber|'
                r'Dialog.getRadioButton|Dialog.getString|Dialog.setInsets|Dialog.setLocation|'
                r'Dialog.show|Ext |File.append|File.close|File.copy|File.dateLastModified|'
                r'File.delete|File.directory|File.exists|File.getName|File.getParent|File.isDirectory|'
                r'File.lastModified|File.length|File.makeDirectory|File.name|'
                r'File.nameWithoutExtension|File.open|File.openAsRawString|File.openAsString|'
                r'File.openDialog|File.openUrlAsString|File.rename|File.saveString|File.separator|'
                r'Fit.doFit|Fit.f|Fit.getEquation|Fit.logResults|Fit.nEquations|Fit.nParams|Fit.p|'
                r'Fit.plot|Fit.rSquared|Fit.showDialog|IJ.currentMemory|IJ.deleteRows|'
                r'IJ.freeMemory|IJ.getToolName|IJ.log|IJ.maxMemory|IJ.pad|'
                r'IJ.redirectErrorMessages|IJ.renameResults|List.clear|List.get|List.getList|'
                r'List.getValue|List.set|List.setCommands|List.setList|List.setMeasurements|'
                r'List.size|Overlay.activateSelection|Overlay.add|Overlay.addSelection|'
                r'Overlay.clear|Overlay.copy|Overlay.drawEllipse|Overlay.drawLabels|'
                r'Overlay.drawLine|Overlay.drawRect|Overlay.drawString|Overlay.hidden|'
                r'Overlay.hide|Overlay.lineTo|Overlay.measure|Overlay.moveSelection|'
                r'Overlay.moveTo|Overlay.paste|Overlay.remove|Overlay.removeSelection|'
                r'Overlay.setPosition|Overlay.show|Overlay.size|Plot.add|Plot.addText|Plot.create|'
                r'Plot.drawLine|Plot.drawNormalizedLine|Plot.drawVectors|Plot.getLimits|'
                r'Plot.getValues|Plot.makeHighResolution|Plot.setAxisLabelSize|'
                r'Plot.setBackgroundColor|Plot.setColor|Plot.setFontSize|Plot.setFormatFlags|'
                r'Plot.setFrameSize|Plot.setJustification|Plot.setLegend|Plot.setLimits|'
                r'Plot.setLimitsToFit|Plot.setLineWidth|Plot.setLogScaleX|Plot.setLogScaleY|'
                r'Plot.setXYLabels|Plot.show|Plot.showValues|Plot.update|Plot.useTemplate|'
                r'Roi.contains|Roi.getBounds|Roi.getCoordinates|Roi.getDefaultColor|'
                r'Roi.getFillColor|Roi.getName|Roi.getProperties|Roi.getProperty|'
                r'Roi.getSplineAnchors|Roi.getStrokeColor|Roi.getType|Roi.move|Roi.setFillColor|'
                r'Roi.setName|Roi.setPolygonSplineAnchors|Roi.setPolylineSplineAnchors|'
                r'Roi.setProperty|Roi.setStrokeColor|Roi.setStrokeWidth|'
                r'Stack.getActiveChannels|Stack.getDimensions|Stack.getDisplayMode|'
                r'Stack.getFrameInterval|Stack.getFrameRate|Stack.getOrthoViewsID|'
                r'Stack.getPosition|Stack.getStatistics|Stack.getUnits|Stack.isHyperstack|'
                r'Stack.setActiveChannels|Stack.setChannel|Stack.setDimensions|'
                r'Stack.setDisplayMode|Stack.setFrame|Stack.setFrameInterval|'
                r'Stack.setFrameRate|Stack.setOrthoViews|Stack.setPosition|Stack.setSlice|'
                r'Stack.setTUnit|Stack.setZUnit|Stack.stopOrthoViews|Stack.swap|String.append|'
                r'String.buffer|String.copy|String.copyResults|String.getResultsHeadings|'
                r'String.paste|String.resetBuffer|String.show|abs|acos|asin|atan|atan2|autoUpdate|'
                r'beep|bitDepth|calibrate|call|changeValues|charCodeAt|close|cos|d2s|'
                r'doCommand|doWand|drawLine|drawOval|drawRect|drawString|dump|endsWith|'
                r'eval|exec|exit|exp|fill|fillOval|fillRect|floodFill|floor|fromCharCode|getArgument|'
                r'getBoolean|getBoundingRect|getCursorLoc|getDateAndTime|getDimensions|'
                r'getDirectory|getDisplayedArea|getFileList|getFontList|getHeight|getHistogram|'
                r'getImageID|getImageInfo|getInfo|getLine|getList|getLocationAndSize|getLut|'
                r'getMetadata|getMinAndMax|getNumber|getPixel|getPixelSize|getProfile|'
                r'getRawStatistics|getResult|getResultLabel|getResultString|getSelectionBounds|'
                r'getSelectionCoordinates|getSliceNumber|getStatistics|getString|getStringWidth|'
                r'getThreshold|getTime|getTitle|getValue|getVersion|getVoxelSize|getWidth|'
                r'getZoom|imageCalculator|indexOf|is|isActive|isKeyDown|isNaN|isOpen|'
                r'lastIndexOf|lengthOf|lineTo|log|makeArrow|makeEllipse|makeLine|makeOval|'
                r'makePoint|makePolygon|makeRectangle|makeSelection|makeText|matches|'
                r'maxOf|minOf|moveTo|nImages|nResults|nSlices|newArray|newImage|newMenu|'
                r'open|parseFloat|parseInt|pow|print|random|rename|replace|requires|reset|'
                r'resetMinAndMax|resetThreshold|restoreSettings|roiManager|round|run|'
                r'runMacro|save|saveAs|saveSettings|screenHeight|screenWidth|selectImage|'
                r'selectWindow|selectionContains|selectionName|selectionType|setAutoThreshold|'
                r'setBackgroundColor|setBatchMode|setColor|setFont|setForegroundColor|'
                r'setJustification|setKeyDown|setLineWidth|setLocation|setLut|setMetadata|'
                r'setMinAndMax|setOption|setPasteMode|setPixel|setRGBWeights|setResult|'
                r'setSelectionLocation|setSelectionName|setSlice|setThreshold|setTool|'
                r'setVoxelSize|setZCoordinate|setupUndo|showMessage|'
                r'showMessageWithCancel|showProgress|showStatus|showText|sin|snapshot|'
                r'split|sqrt|startsWith|substring|tan|toBinary|toHex|toLowerCase|toScaled|toString|'
                r'toUnscaled|toUpperCase|toolID|updateDisplay|updateResults|wait|waitForUser)\b', Name.Builtin),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'`', String.Backtick, 'interp'),
            (r'[$a-zA-Z_][\w.\-:$]*\s*[:=]\s', Name.Variable, 'slashstartsregex'),
            (r'@[$a-zA-Z_][\w.\-:$]*\s*[:=]\s', Name.Variable.Instance, 'slashstartsregex'),
            (r'@', Name.Other, 'slashstartsregex'),
            (r'@?[$a-zA-Z_][\w-]*', Name.Other, 'slashstartsregex'),
        ],
        'interp': [
            (r'`', String.Backtick, '#pop'),
            (r'\\\\', String.Backtick),
            (r'\\`', String.Backtick),
            (r'\$\{', String.Interpol, 'interp-inside'),
            (r'\$', String.Backtick),
            (r'[^`\\$]+', String.Backtick),
        ],
        'interp-inside': [
            # TODO: should this include single-line comments and allow nesting strings?
            (r'\}', String.Interpol, '#pop'),
            include('root'),
        ],            

    }
