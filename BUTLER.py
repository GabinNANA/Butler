# - coding: utf-8 --

import tensorflow as tf
from tkinter.filedialog import *
import tkinter.font as tkFont
import shutil
from tkinter.filedialog import *

fenetre = Tk()
fenetre.geometry("800x700+350+50")
fenetre.title("BUTLER")
counter = 0
rep = ''


class Interface(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    font10 = tkFont.Font(family='Helvetica', size=25, weight='bold')
    font1 = tkFont.Font(family='Helvetica', size=15, weight='normal')

    test = "\nBUTLER...\n L'IA range pour vous\n"
    label = Label(fenetre, text=test, fg='teal')
    label.configure(font=font10)
    label.pack()

    test = "Veuillez entrer ce que vous voulez rechercher sur vos photos\n puis choisissez le repertoire des photos\n"
    label = Label(fenetre, text=test, fg='black')
    label.configure(font=font1)
    label.pack()

    value = StringVar()
    value.set("inspire")
    entree = Entry(fenetre, textvariable=value, width=30)
    entree.pack()

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        font1 = tkFont.Font(family='Helvetica', size=15, weight='normal')
        self.pack(fill=BOTH)
        self.btnchoixrep = Button(self, text='Repertoire à analyser', fg="black", command=self.choixrep)
        self.btnchoixrep.pack(side="top")

        test = "\nVeillez choisir le repertoire dans lequel se fera\n le classement de fichiers par extensions\n"
        label = Label(self, text=test, fg='black')
        label.configure(font=font1)
        label.pack()
        btnchoixrep = Button(self, text='Classement extensions', fg="black", command=self.butler)
        btnchoixrep.pack()


    def image(self, rep):
        if len(rep) > 0:
            print("vous avez choisi le repertoire %s" % rep)
        dossier = rep + '/Images'
        print(dossier)
        if not os.path.exists(dossier):
            os.mkdir(dossier)
            dossier_cible = dossier
        else:
            dossier_cible = dossier

        for element in os.listdir(rep):
            print(element)
            if element.endswith('.jpg') or element.endswith('.png') or element.endswith('.gif'):
                if os.path.exists(dossier_cible + '/' + element):
                    date_masource = os.path.getmtime(rep + '/' + element)
                    date_macible = os.path.getmtime(dossier_cible + '/' + element)
                    if date_masource > date_macible:
                        shutil.copy(rep + '/' + element, dossier_cible)
                        os.remove(rep + '/' + element)
                        print(element, '\t', "mis à jour")

                    else:
                        continue
                elif os.path.exists(dossier_cible + '/' + element) == False:
                    shutil.copy(rep + '/' + element, dossier_cible)
                    os.remove(rep + '/' + element)
                    print(element, '\t', "copié")
                else:
                    continue
        print("Analyse terminée")
    def texte(self, rep):
        if len(rep) > 0:
            print("vous avez choisi le repertoire %s" % rep)
        dossier = rep + '/Documents texte'
        print(dossier)
        if not os.path.exists(dossier):
            os.mkdir(dossier)
            dossier_cible = dossier
        else:
            dossier_cible = dossier

        for element in os.listdir(rep):
            print(element)
            if element.endswith('.docx') or element.endswith('.txt') or element.endswith('.doc'):
                if os.path.exists(dossier_cible + '/' + element):
                    date_masource = os.path.getmtime(rep + '/' + element)
                    date_macible = os.path.getmtime(dossier_cible + '/' + element)
                    if date_masource > date_macible:
                        shutil.copy(rep + '/' + element, dossier_cible)
                        os.remove(rep + '/' + element)
                        print(element, '\t', "mis à jour")

                    else:
                        continue
                elif os.path.exists(dossier_cible + '/' + element) == False:
                    shutil.copy(rep + '/' + element, dossier_cible)
                    os.remove(rep + '/' + element)
                    print(element, '\t', "copié")
                else:
                    continue
        print("Analyse terminée")
    def video(self, rep):
        if len(rep) > 0:
            print("vous avez choisi le repertoire %s" % rep)
        dossier = rep + '/Vidéos'
        print(dossier)
        if not os.path.exists(dossier):
            os.mkdir(dossier)
            dossier_cible = dossier
        else:
            dossier_cible = dossier

        for element in os.listdir(rep):
            print(element)
            if element.endswith('.avi') or element.endswith('.mp4'):
                if os.path.exists(dossier_cible + '/' + element):
                    date_masource = os.path.getmtime(rep + '/' + element)
                    date_macible = os.path.getmtime(dossier_cible + '/' + element)
                    if date_masource > date_macible:
                        shutil.copy(rep + '/' + element, dossier_cible)
                        os.remove(rep + '/' + element)
                        print(element, '\t', "mis à jour")

                    else:
                        continue
                elif os.path.exists(dossier_cible + '/' + element) == False:
                    shutil.copy(rep + '/' + element, dossier_cible)
                    os.remove(rep + '/' + element)
                    print(element, '\t', "copié")
                else:
                    continue
        print("Analyse terminée")

    def PDF(self, rep):
        if len(rep) > 0:
            print("vous avez choisi le repertoire %s" % rep)
        dossier = rep + '/PDF'
        print(dossier)
        if not os.path.exists(dossier):
            os.mkdir(dossier)
            dossier_cible = dossier
        else:
            dossier_cible = dossier

        for element in os.listdir(rep):
            print(element)
            if element.endswith('.pdf'):
                if os.path.exists(dossier_cible + '/' + element):
                    date_masource = os.path.getmtime(rep + '/' + element)
                    date_macible = os.path.getmtime(dossier_cible + '/' + element)
                    if date_masource > date_macible:
                        shutil.copy(rep + '/' + element, dossier_cible)
                        os.remove(rep + '/' + element)
                        print(element, '\t', "mis à jour")

                    else:
                        continue
                elif os.path.exists(dossier_cible + '/' + element) == False:
                    shutil.copy(rep + '/' + element, dossier_cible)
                    os.remove(rep + '/' + element)
                    print(element, '\t', "copié")
                else:
                    continue
        print("Analyse terminée")
    def butler(self):
        global rep
        rep = askdirectory(initialdir="/", title='Choisissez un repertoire')
        self.image(rep)
        self.PDF(rep)
        self.video(rep)
        self.texte(rep)

    def choixrep(self):
        global rep
        rep = askdirectory(initialdir="/", title='Choisissez un repertoire')
        if len(rep) > 0:
            print("vous avez choisi le repertoire %s" % rep)

        for element in os.listdir(rep):
            if element.endswith('.jpg') or element.endswith('.png'):
                print("'%s' est un fichier image" % element)
                lien = rep + '/' + element
                self.clique(lien, self.entree.get(), element)
        element=0
        print(element)
        Label(fenetre, text="Analyse Terminée", fg='teal').pack()

    def clique(self, image_path, resultat, element):
        dossier = rep + '/' + resultat
        print(dossier)
        if not os.path.exists(dossier):
            os.mkdir(dossier)
            dossier_cible = dossier
        else:
            dossier_cible = dossier
        print(image_path)
        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        variable = '%'
        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("./labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("./output.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
                                   {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                variable = ('Il s\'agit d\'un drône %s à %.5f' % (human_string, score * 100)) + variable
                break
        if (human_string==resultat)and (score>=0.5):
            dossier_source = rep
            if os.path.exists(dossier_cible + '/' + element):
                date_masource = os.path.getmtime(dossier_source + '/' + element)
                date_macible = os.path.getmtime(dossier_cible + '/' + element)
                if date_masource > date_macible:
                    shutil.copy(dossier_source + '/' + element, dossier_cible)
                    os.remove(dossier_source + '/' + element)
                    print(element, '\t', "mis à jour")
            elif os.path.exists(dossier_cible + '/' + element) == False:
                shutil.copy(dossier_source + '/' + element, dossier_cible)
                os.remove(dossier_source + '/' + element)
                print(element, '\t', "copié")

interface = Interface(fenetre)
interface.mainloop()
interface.destroy()