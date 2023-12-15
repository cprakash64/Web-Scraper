from instalooter.looters import ProfileLooter
import datetime
import dateutil.relativedelta

# instalooter_test downloads videos posted by tube.indian in the last month

# Instanciate 
looter = ProfileLooter("tube.indian", videos_only=True, template="{id}-{username}-{width}-{height}")
looter.login("64memeshub", "@Markchotugreat64")

today = datetime.date.today()
thismonth = (today, today - dateutil.relativedelta.relativedelta(days=28))

looter.download('/Users/chotu/Documents/YouTube Content', media_count=50, timeframe=thismonth)