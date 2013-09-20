# mixpandas

Get data from Mixpanel's Raw Data Export API into a Pandas DataFrame for
powerful custom analysis. Use `read_events` to query your data. Specify 
event names, date ranges or other filters to control selection.
Consult the documentation for detailed use.

Mixpandas wraps [Mixpanel's API client](https://mixpanel.com/site_media//api/v2/mixpanel.py) with a few modifications
documented in the code.

### Example
An app tracks a `submit rating` event with a `stars` property indicating the rating.
Find each user's average rating over a specified time span.

    >>> keys = (MIXPANEL_API_KEY, MIXPANEL_API_SECRET)
    >>> df = mixpandas.read_events(keys, events='submit rating', start='9/8/2013', end='9/15/2013')
    >>> df.groupby('distinct_id')['stars'].mean()
    distinct_id
    10             3.00000
    12             4.50000
    15             4.75000
    2              4.00000
    23             2.66667
    27             5.00000
    ...
    
The `start` and `end` dates are parsed with `pandas.to_datetime` and converted to the proper Mixpanel format. This 
allows you to think less about how to specify the dates and just get the data you want. The following are just a few
ways to do the same thing:

    >>> df = mixpandas.read_events(keys, events='submit rating', start='9/8/2013')
    >>> df = mixpandas.read_events(keys, events='submit rating', start='2013-9-8')
    >>> df = mixpandas.read_events(keys, events='submit rating', start='Sept 8, 2013')

Mixpanel includes the time as a property of each tracked event.  Mixpandas converts this `time` property to
Pandas `Timestamp` objects enabling powerful slicing and other time series analysis.

    >>> df.set_index('time', inplace=True, drop=False)
    
    # Grab arbitrary time spans of the data
    >>> df['9/12/2013':'2013-09-15']  # Dates can be specified in many ways
    
    # Compute the 5 day window moving average of number of ratings submissions
    >>> counts = df.groupby(df['time'].map(lambda x: x.date())).size()  # Group data by day, get counts
    >>> counts.index = pd.DatetimeIndex(counts.index)  # Get back the DatetimeIndex
    >>> counts = counts.resample('D')  # Re-sample every day in case some days have none
    >>> pd.rolling_mean(counts, 5)  # Compute the 5 day moving average
