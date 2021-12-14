import pandas as pd
import main
import requests
object = main.Scraper()


token = "OTEzNDkxNTY2NjMzNTc0NDcy.YZ_RjQ.8kP65jUJ_i6psDa8OqCY3iQt3Tc"

def send_discord_notification(message):
    url = 'https://discord.com/api/v9/channels/920009890351677440/messages'
    data = {
        'content' : message
    }
    header = {
        'authorization' : token
    }

    requests.post(url, data=data, headers=header)


def get_data_using_id(file_name, start_id, end_id):
    all_ids = list(pd.read_csv("{}".format(file_name)).iloc[:,0])
    required_ids = all_ids[start_id : end_id]
    
    filename = "{}-{}-data.csv".format(start_id, end_id)

    for i in range(len(required_ids)):
        if(len(str(required_ids[i])) != 8):
            s = ""
            for j in range(8-len(str(required_ids[i]))):
                s+="0"
            s+=str(required_ids[i])
            url = "https://www.pagesjaunes.fr/pros/" + s

            object.extract_details('{}'.format(url))
            #message = "Scraped for url : {}".format(url)
            #send_discord_notification(message)

        
        else:
            url = "https://www.pagesjaunes.fr/pros/{}".format(required_ids[i])
            object.extract_details('{}'.format(url))
            #message = "Scraped for url : {}".format(url)
            #send_discord_notification(message)

            
    
    column = ["url", "id", "nom_societe", "adresse", "code_postal", "ville", "rubrique", "siret", "dernire_modif", "tva_intra", "principaux_dirigeants", "rating", 'review', "telephone", 'mobile', "fax", "website", "activities", 'prestations', "produits", "description", "horaires", "budget", "tarif_nuit", "cuisine", "ambiance", "formules", "nom_du_chef", "references_et_guides", "moyens_de_paiement", "nbre_etoile_hotel", "nbre_chambres", "marque", "capacite_accueil", "info_pratique", "services_loisirs", "clientele"]
            
    df=pd.DataFrame(object.scraped_data,columns=column)
    df.to_csv(filename,index=False)  # If excel file of output data is required.
    return df
    
    df = get_data_using_id('pj_index_list_NEW.csv',1,10000)
    if df.shape[0] != 10000:
        send_discord_notification("Error")
    else:
        message = "Scraped for ids {} - {}".format(start_id, end_id)
        send_discord_notification(message)
