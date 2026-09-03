from tkinter import messagebox
import constants
import requests
import json


class Requester:

    def make_request(self, word, operation):
        url = r"https://api.datamuse.com/words"
        word = word.lower()
        list_words = word.split(" ")
        # we want to check if there are more than 2 words written -> if so just introduce an error message
        if len(list_words) != 1:
            messagebox.showerror("ONE WORD", "Please enter a single word and not a sentence")
            return
        param_syn = {"rel_syn": word}
        param_ant = {"rel_ant": word}
        param_hom = {"rel_hom": word}
        #hypernims -> kind of that word
        param_hyph = {"rel_spc": word}

        params = {
            constants.ABBREVIATIONS[0]: param_syn,
            constants.ABBREVIATIONS[1]: param_ant,
            constants.ABBREVIATIONS[2]: param_hom,
            constants.ABBREVIATIONS[3]: param_hyph,
        }
        response = requests.get(url, params=params[operation])
        try:
            return response.json()
        except ValueError:
            messagebox.showerror("ERROR", "Something wrong with the server")
            print(response.text)
            return None

    def extract_first_results(self, result_api):
        if result_api is None:
            return
        if len(result_api) >=5:
            summary_json = result_api[:5]
        else:
            summary_json = result_api
        results = []
        for res in summary_json:
            results.append(res["word"])
        return results


