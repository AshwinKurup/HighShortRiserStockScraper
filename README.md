# HighShortRiserStockScraper
 Looks for stocks with high short float that have a pattern that looks like ENPH April-ish or whenever I first looked at it


testidea.py prints a list of all the finviz chart pic links for the stocks, copy paste that into testin.py's TEST_stock_chart_link variable or idk what it's called. 

then use the makeChartList() at the bottom to see 0, 60 then 60, 120, it's in multiples of 60 cos tkinter can't take anymore 100*100 pix pics i the frame it produces. 