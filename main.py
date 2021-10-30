import time
import os
import cultivate

def main(amount):
    for i in range(amount):
        planted_crop = cultivate.plant()
        print('\n', '-'*50)
        os.system(f'git commit -am "#{planted_crop}"')
        os.system('git push --all')
        time.sleep(0.1)

crop_amount = int(input('Crop Amount: '))
    
if __name__ == '__main__':
    main(crop_amount)