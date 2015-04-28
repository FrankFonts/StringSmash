#!/usr/bin/env python 


presetDict = {
    
    # ascender subset
    'Ascenders, Latin' : 'b d f h k l thorn'.split(' '),
    
    # adescender subset
    'Descenders, Latin' : 'g j p q'.split(' '),
    
    # diagonal lowercase subset
    'Diagonals, Latin lowercase' : 'k v w x y'.split(' '),
    
    # diagonal uppercase subset
    'Diagonals, Latin uppercase' : 'K V W X Y'.split(' '),
    
    # Basic Latin uppercase
    'Basic Latin uppercase' : 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AE Eth OE'.split(' '),
    
    # Basic Latin lowercase
    'Basic Latin lowercase' : 'a b c d e f g h i j k l m n o p q r s t u v w x y z ae et oe thorn'.split(' '),
    
    # Latin uppercase
    'Latin extended uppercase' : 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Agrave Aacute Acircumflex Atilde Adieresis Amacron Abreve Acaron Aring Aringacute Aogonek AE AEacute Cacute Ccedilla Ccircumflex Ccaron Cdotaccent Dcaron Dcroat Eth Egrave Eacute Ecircumflex Ecaron Edieresis Emacron Ebreve Edotaccent Eogonek Gcircumflex Gbreve Gdotaccent Gcommaaccent Hcircumflex Hbar Igrave Iacute Icircumflex Itilde Idieresis Imacron Ibreve Idotaccent Iogonek IJ Jcircumflex Kcommaaccent Lacute Lcaron Lcommaaccent Lslash Ldot Nacute Ncaron Ntilde Ncommaaccent Eng Ograve Oacute Ocircumflex Otilde Odieresis Omacron Obreve Ohungarumlaut Oslash Oslashacute OE Thorn Racute Rcaron Rcommaaccent Sacute Scircumflex Scaron Scedilla Scommaaccent Tcaron Tcommaaccent uni021A Tbar Ugrave Uacute Ucircumflex Utilde Udieresis Umacron Ubreve Uring Uhungarumlaut Uogonek Wgrave Wacute Wcircumflex Wdieresis Ygrave Yacute Ycircumflex Ydieresis Zacute Zcaron Zdotaccent'.split(' '),
    
    # Latin lowercase
    'Latin extended lowercase' : 'a b c d e f g h i j k l m n o p q r s t u v w x y z fi fl f_f f_f_i f_f_l agrave aacute acircumflex atilde adieresis amacron abreve acaron aring aringacute aogonek ae aeacute cacute ccedilla ccircumflex ccaron cdotaccent dcaron dcroat eth egrave eacute ecircumflex ecaron edieresis emacron ebreve edotaccent eogonek gcircumflex gbreve gdotaccent gcommaaccent hcircumflex hbar dotlessi igrave iacute icircumflex itilde idieresis imacron ibreve iogonek ij jcircumflex kcommaaccent kgreenlandic lacute lcaron lcommaaccent lslash longs ldot nacute ncaron ntilde ncommaaccent napostrophe eng ograve oacute ocircumflex otilde odieresis omacron obreve ohungarumlaut oslash oslashacute oe thorn racute rcaron rcommaaccent sacute scircumflex scaron scedilla scommaaccent germandbls tcaron tcommaaccent uni021B tbar ugrave uacute ucircumflex utilde udieresis umacron ubreve uring uhungarumlaut uogonek wgrave wacute wcircumflex wdieresis ygrave yacute ycircumflex ydieresis zacute zcaron zdotaccent'.split(' '),
    
    # Default figures
    'Figures, default' : 'zero one two three four five six seven eight nine'.split(' '),
    
    # Tabular figures
    'Figures, tabular' : 'zero.tab one.tab two.tab three.tab four.tab five.tab six.tab seven.tab eight.tab nine.tab'.split(' '),
    
    # Punctuation
    'Punctuation' : 'period comma colon semicolon hyphen'.split(' '),
    
    # Parentheses
    'Parentheses' : 'braceleft braceright bracketleft bracketright parenleft parenright'.split(' '),
    
    # Quotation
    'Quotation' : 'guillemotleft guillemotright guilsinglleft guilsinglright quotedblbase quotedblleft quotedblright quoteleft quoteright quotesinglbase'.split(' '),
}


delimDict = {
    'H' : ['H'],
    
    'O' : ['O'],
    
    'HH' : ['H', 'H'],
    
    'HO' : ['H', 'O'],
    
    'OH' : ['O', 'H'],
    
    'OO' : ['O', 'O'],
    
    'n' : ['n'],
    
    'o' : ['o'],
    
    'nn' : ['n', 'n'],
      
    'oo' : ['o', 'o'],
    
    'no' : ['n', 'o'],
    
    'on' : ['o', 'n'],
    
    'zero, default' : ['zero'],
    
    'zero, tabular' : ['zero.tab'],
}

guessDelimDict=presetDict