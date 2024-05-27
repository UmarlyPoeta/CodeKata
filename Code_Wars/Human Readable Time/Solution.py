def make_readable(seconds):
    hours=seconds//3600
    seconds=seconds-(hours*3600)
    minutes=seconds//60
    seconds=seconds-(minutes*60)
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"