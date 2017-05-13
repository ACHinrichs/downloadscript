import downloadscript as ds
import config_private as config

for lecture in config.lectures:
    print("NOW FETCHING "+lecture[0])
    ds.REG_FINDSTRING   = lecture[1]
    ds.REG_SUBSTRING    = lecture[2]
    ds.URL_MATERIALS    = lecture[3]
    ds.URL_LECTURENOTES = lecture[4]
    ds.OUT_DIR          = lecture[5]
    ds.download()
print("All done")
