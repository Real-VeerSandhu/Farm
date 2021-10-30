import time
import os
import cultivate

def main():
    for i in range(3):
        planted_crop = cultivate.plant()
        os.system(f'git commit -am "#{planted_crop}"')
        os.system('git push --all')
        time.sleep(3)

    
if __name__ == '__main__':
    main()