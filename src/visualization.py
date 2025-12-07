import plotly.express as px

def plot_top_stations(df, title_suffix=""):
    """
    Generates a horizontal bar chart for top start stations.
    """
    if df.empty:
        return None
        
    fig = px.bar(
        df,
        x='Trip Count',
        y='Start Station Name',
        orientation='h',
        text='Trip Count',
        title=f"Top 10 Start Stations {title_suffix}",
        color='Trip Count',
        color_continuous_scale='Blues'
    )
    
    # Optimize Layout
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'}, 
        height=500
    )
    
    return fig

def plot_peak_hours(df, title_suffix=""):
    """
    Generates a bar chart for trips by hour of day.
    """
    if df.empty:
        return None
        
    fig = px.bar(
        df,
        x='Hour',
        y='Trip Count',
        title=f"Trips by Hour of Day {title_suffix}",
        labels={'Hour': 'Hour of Day (0-23)', 'Trip Count': 'Number of Trips'},
        text='Trip Count'
    )
    
    # Optimize Layout
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        height=450
    )
    
    return fig