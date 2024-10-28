

if __name__ == "__main__":
    user = os.environ['USER_PHONE']
    password = os.environ['USER_PWD']
    # step = str(randint(int(os.environ['STEP_MIN']), int(os.environ['STEP_MAX'])))
    step = os.environ['STEP']
    # step = str(randint(10123, 12302)) 
    main(user，password，step)
