import plotly.graph_objects as go
from plotly.subplots import make_subplots

class CandleStickFigure():
    def __init__(self, 
                 df, 
                 row_heights = [1],  
                 column_widths = [1],
                 tag_name = None):
        self.nrows = len(row_heights)
        self.ncols = len(column_widths)
        
        self.df = df
        self.fig = make_subplots(
            rows=self.nrows, cols=self.ncols,
            shared_xaxes=True,
            vertical_spacing=0.05,
            row_heights=row_heights, 
            column_widths=column_widths, 
        )
        self.tag_name = "Data" if tag_name == None else tag_name
    
    def add_candlestick(self, row = 1, col = 1):
        if "low" in self.df and "high" in self.df and "close" in self.df and "open" in self.df:
            cols = ["low", "high", "close", "open"]
        elif "Low" in self.df and "High" in self.df and "Close" in self.df and "Open" in self.df:
            cols = ["Low", "High", "Close", "Open"]
        else:
            print("cols not found")
            return None
        
        self.fig.add_trace(
            go.Candlestick(
                x = self.df.index,
                low = self.df[cols[0]],
                high = self.df[cols[1]],
                close = self.df[cols[2]],
                open = self.df[cols[3]],
                name = self.tag_name),
                row= row, col= col)
        
        for i in range(1, self.nrows + 1):
            self.fig.update_layout(
                dict(        
                    {"xaxis{:.0f}".format(i) : {"rangeslider": {"visible": False}}}
                )
            )

    @staticmethod
    def add_difference(series):
        diff = (100*series.diff().shift(-1) / series).shift(1)
        diff_colors = diff.apply(lambda x: "red" if x <0 else "green").to_list()
        hovertemplate = ["{:,.2f} (%{:.2f})".format(i,j) for i,j in zip(series.to_list(), diff.to_list())]
        return hovertemplate, diff_colors

    def add_trace_bar(self, 
                      series_name, row, col,
                      opacity = 1.0):
        if series_name in self.df:
            plotting = getattr(go, "Bar")
            hovertemplate, diff_colors = self.add_difference(self.df[series_name])
            self.fig.add_trace(
                plotting(
                    x=self.df[series_name].index,
                    y=self.df[series_name],
                    name = series_name,
                    opacity = opacity,
                    marker_color = diff_colors,
                    hovertemplate = hovertemplate
                ), row=row, col=col)
            
        else:
            print(series_name, "is not in dataframe")
            return None

    def add_hline(self, bounds, 
                  row, col, 
                  opacity = 1.0,):
        for i in bounds:
            self.fig.add_trace(
                go.Scatter(
                    name='',
                    x = [self.df.index[0], self.df.index[-1]],
                    y = [i,i],
                    mode = "lines",
                    #marker = dict(color = 'rgba(80, 26, 80, 0.5)'),
                    opacity=opacity,
                    showlegend=False,
                    line = dict(color='rgb(80, 26, 80)', dash='dash')
                    ),
                row=row, col=col)

    def add_trace_scatter(
            self, series_name, row, col,
            opacity = 1.0, 
    ):
        if series_name in self.df:
            plotting = getattr(go, "Scatter")
            self.fig.add_trace(
                plotting(
                    x=self.df[series_name].index,
                    y=self.df[series_name],
                    name = series_name,
                    opacity = opacity,
                    line_color = None,
                ), row=row, col=col)
            
        else:
            print(series_name, "is not in dataframe")
            return None


    def add_trace_area_fibolines(
            self, series_name, row, col,
            opacity = 1.0, 
    ):
        fibo_area_colors = {
            "fl02": 'rgba(127,127,127, 0.2)',
            "fl04": 'rgba(31,119,180, 0.2)',
            "fl05": 'rgba(188,189,34, 0.2)',
            "fl06": 'rgba(44,160,44, 0.2)',
            "fl08": 'rgba(255,127,14, 0.2)',
            "fl10": 'rgba(214,39,40, 0.2)',
            "fl00": None,
        }
        fibo_line_colors = {
            "fl02": 'rgba(127,127,127, 0.2)',
            "fl04": 'rgba(31,119,180, 0.2)',
            "fl05": 'rgba(188,189,34, 0.2)',
            "fl06": 'rgba(44,160,44, 0.2)',
            "fl08": 'rgba(255,127,14, 0.2)',
            "fl10": 'rgba(214,39,40, 0.2)',
            "fl00": 'rgba(127,127,127, 0.2)',
        }

        if series_name in self.df and series_name[:2] == "fl":
            plotting = getattr(go, "Scatter")
            self.fig.add_trace(
                plotting(
                    x=self.df[series_name].index,
                    y=self.df[series_name],
                    name = series_name,
                    opacity = opacity,
                    line_color = fibo_line_colors[series_name] if series_name[:2] == "fl" else None,
                    fill='tonexty' if series_name[:2] == "fl" and series_name[2:4] != "00"  else None,
                    fillcolor = fibo_area_colors[series_name] if series_name[:2] == "fl" else None,
                    showlegend=False if series_name[:2] == "fl" else True
                ), row=row, col=col)
            
        else:
            print(series_name, "is not in dataframe")
            return None



    def _remove_days_bist(self):
        ###
        ## Tatilleri de buraya ekle !!
        ###
        # holidays_data = pd.to_datetime(list(holidays.TR(range(2020,2025)).keys())).strftime("%Y-%m-%d").tolist()
        # dates = pd.date_range(
        #     self.df.index[0].strftime("%Y-%m-%d"),
        #     self.df.index[-1].strftime("%Y-%m-%d"),
        #     freq = "1d")
        
        # out_of = []
        # for i in dates:
        #     if i.strftime("%Y-%m-%d") in holidays or i.weekday() in [5, 6]:
        #         out_of.append(i.strftime("%Y-%m-%d"))

        rangebreaks = [
            dict(bounds=[18.5, 9.5], pattern="hour"), 
            dict(bounds=["sat", "mon"]), 
#            dict(values=holidays_data)
            ]
        self.fig.update_xaxes(rangebreaks=rangebreaks)



    def update_settings(self, height = 700):
        self.fig.update_layout(
            height = height,
            hovermode = "x unified",)
        self.fig.update_traces(xaxis="x{:.0f}".format(self.nrows))
        self.fig.update_yaxes(showgrid=False)




