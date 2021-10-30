import time
import os
import cultivate

def main():
    for i in range(3):
        planted_crop = cultivate.plant()
        print('-'*50)
        os.system(f'git commit -am "#{planted_crop}"')
        os.system('git push --all')
        print('-'*50)
        time.sleep(0.1)

    
if __name__ == '__main__':
    main()