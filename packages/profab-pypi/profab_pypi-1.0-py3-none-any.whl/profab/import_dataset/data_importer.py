# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 01:00:05 2021

@author: Sameitos
"""

import os, re
import random
from zipfile import ZipFile
from profab.utils.imp_split_form import separator,  self_data, _classif_data_import, download_data

class cls_data_loader():
    
    def __init__(self,ratio,protein_feature,main_set,set_type,label,pre_determined):
        
        """
            Parameters:
                main_set: {ec_dataset, go_dataset}, folder includes its corresponding data name
        """
        self.ratio = ratio
        self.protein_feature = protein_feature
        self.set_type = set_type
        self.label = label
        self.pre_determined = pre_determined
        self.main_set = main_set#{ec_dataset,go_dataset}: Indicated which data folder will be opened.
        self.server_path = "https://liverdb.kansil.org/profab"
        self.raiser()
        
        
    def raiser(self):
        
        """
            It is to raise the exceptions that can be occured because of false attributes enter.
        """
        if self.set_type not in ['random','similarity','temporal']:
         	raise AttributeError('Please enter correct set_type. Options are: "random, similarity, temporal"')
        if self.set_type == 'similarity': self.set_type = 'target'
        if self.set_type == 'temporal': 
            self.pre_determined = True
        
        if self.protein_feature not in ['paac', 'aac', 'gaac', 'ctdt','ctriad','socnumber', 'kpssm']:
         	raise AttributeError('Please enter correct protein_feature. Options are: "paac, aac, gaac, ctdt, ctriad, socnumber, kpssm"')
        if self.protein_feature == 'kpssm': self.protein_feature = 'k_separated_bigrams_pssm'
        
        
        if self.label not in [None,'positive','negative','positive_negative']:
            raise AttributeError('Please enter correct label. Options are: "None, positive, negative"')
        
        
        if self.pre_determined:
            if type(self.ratio) not in [None,float]:
                raise AttributeError(
                    f'Please enter ratio value in true type. Options: "None, float" for pre_determined = True or '
                    f'set_type = temporal')        
        elif not self.pre_determined:
            if type(self.ratio) not in [None,float,list]:
                raise AttributeError(
                    'Please enter ratio value in true type. Options: "None, float and list" for pre_determined = False')
        
        
    def get_data(self,data_name):
        
        """
            Take attributes and prepare datasets according to them. If no data is available at local, then is dowloaded
            
        """
        
        #Check whether given data name and its family are matched
        if self.main_set[:2].lower() != data_name[:2].lower():
            
            raise FileNotFoundError(f'Please enter a correct data name: {data_name} not found in {self.main_set[:2].upper()} sets')
        
        pPath = os.path.split(os.path.realpath(__file__))[0]
        
        #Check whether there is save folder
        if not os.path.exists(self.main_set):
            os.makedirs(self.main_set)
        #Check whether there is a folder named main set
        if os.path.isfile(self.main_set + '/' + data_name + '.zip'):
            data_path = self.main_set + '/' + data_name + '.zip'

            
        #If no given data name, then data will be downloaded from the server to folder of main set.
        #This condition also looks for if data is available in server.
        else:
            print(f'No local dataset for {data_name} is available. Downloading from server ...')
            
            data_server_path = self.server_path + '/' + self.main_set + '/' + data_name + '.zip'
            
            data_path = self.main_set + '/' + data_name + '.zip'
            
            download_data(data_server_path,data_path)
            
        #Rest is checking wheter files are optional and preparing datasets
        if not self.pre_determined:

            pos_file = data_name + '/' + self.set_type + '_positive_' + self.protein_feature + '.txt'
            neg_file = data_name + '/' + self.set_type + '_negative_' + self.protein_feature + '.txt'
            
            if pos_file not in ZipFile(data_path).namelist() or neg_file not in ZipFile(data_path).namelist():
                self.look_options(ZipFile(data_path).namelist(), data_name)

            pX,nX,X,y = _classif_data_import(zip_data = data_path, pos_file = 
                                               pos_file, neg_file = neg_file, label = self.label)


            if self.label == 'positive':
                return pX
            elif self.label == 'negative':
                return nX
            
            else:
                trdn = list(zip(X,y))
                random.shuffle(trdn)
                X,y = zip(*(trdn))
                
                if not self.ratio:
                    return X,y
                if self.ratio is not None:
                    return separator(ratio = self.ratio,X = X,y =y)
                else:
                    raise AttributeError(
                        'Please enter ratio value in true type. Options: "None, float and list" for pre_determined = False')
                    
        else:
        
            pos_file = data_name + '/' + self.set_type + '_positive_' + self.protein_feature + '.txt'
            neg_file = data_name + '/' + self.set_type + '_negative_' + self.protein_feature + '.txt'
            
            if pos_file not in ZipFile(data_path).namelist() or neg_file not in ZipFile(data_path).namelist():
                
                self.look_options(ZipFile(data_path).namelist(), data_name)
                
            
            
            train_pos_idx = data_name + '/' + self.set_type + '_positive_train_indices.txt'
            train_neg_idx = data_name + '/' + self.set_type + '_negative_train_indices.txt'

            test_pos_idx = data_name + '/' + self.set_type + '_positive_test_indices.txt'
            test_neg_idx = data_name + '/' + self.set_type + '_negative_test_indices.txt'
                        

            tpX,tnX,tX,ty = _classif_data_import(zip_data = data_path, pos_file = pos_file,
                                                         neg_file = neg_file, pos_indices = train_pos_idx,
                                                         neg_indices = train_neg_idx,
                                                         label = self.label)
            tepX,tenX,teX,tey = _classif_data_import(zip_data = data_path, pos_file = pos_file,
                                                               neg_file = neg_file,
                                                               pos_indices = test_pos_idx,
                                                               neg_indices = test_neg_idx,
                                                               label = self.label)
                

            return_pos = [tpX,tepX]
            return_neg = [tnX,tenX]
            
            if self.set_type == 'temporal':
                valid_pos_idx = data_name + '/' + self.set_type + '_positive_validation_indices.txt'
                valid_neg_idx = data_name + '/' + self.set_type + '_negative_validation_indices.txt'
                
                vpX,vnX,vX,vy = _classif_data_import(zip_data = data_path,pos_file = pos_file, neg_file = neg_file, 
                    pos_indices = valid_pos_idx,neg_indices = valid_neg_idx,
                    label = self.label)            
                
                return_pos.extend([vpX])
                return_neg.extend([vnX])

            
            if self.label == 'positive':
                return return_pos
            elif self.label == 'negative':
                return return_neg
            elif self.label == 'positive_negative':
                return return_pos.extend(return_neg)
            else:
                
                trdn = list(zip(tX,ty))
                random.shuffle(trdn)
                tX,ty = zip(*trdn)
            
                terdn = list(zip(teX,tey))
                random.shuffle(terdn) 
                teX,tey = zip(*terdn)
            
                if self.set_type == 'temporal':
                    vrdn = list(zip(vX,vy))
                    random.shuffle(vrdn)
                    vX,vy = zip(*vrdn)
                    return tX,teX,vX,ty,tey,vy
            
            
                if self.ratio is None:
                    return tX,teX,ty,tey
                    
                if type(self.ratio) == float:
                    tX,vX,ty,vy = separator(ratio = self.ratio,X = tX,y = ty)
                    return tX,teX,vX,ty,tey,vy
                
                else:
                    raise AttributeError(
                        'Please enter ratio value in true type. Options: "None, float" for pre_determined = True')
                    
    def look_options(self,name_list,data_name):
        """
            Look for options for set_type and protein features found 
            in zip file and return them. It is to learn what is inside
            of zip file.
        """
        avai_sets, avai_prots = set(),set()
        for names in name_list:
            if not re.search('indices',names):
                row = re.split('_|/',names)
                avai_sets.add(row[2])
                avai_prots.add(row[-1][:-4])
        if 'target' in avai_sets:
            avai_sets.remove('target')
            avai_sets.add('similarity')
        if 'k_separated_bigrams_pssm' in avai_prots:
            avai_prots.remove('k_separated_bigrams_pssm')
            avai_prots.add('kpssm')
        
        if self.protein_feature == 'k_separated_bigrams_pssm': self.protein_feature = 'kpssm'
        if self.set_type == 'target': self.set_type = 'similarity'
        if self.set_type not in avai_sets:
            raise Exception(
                
                f'!!Under maintenance!! Specified set type "{self.set_type}" is not available for {data_name}. '
                f'Available set_type options: {avai_sets}')
        elif self.protein_feature not in avai_prots:
            raise Exception(
                
                f'!!Under maintenance!! Specified protein feature type '
                f'"{self.protein_feature}" type is not available for {data_name}. '
                f'Available protein_feature options: {avai_prots}')
        
        else:
            raise Exception(
                
                f'!!Under maintenance!! Specified set type "{self.set_type}" and protein feature type '
                f'"{self.protein_feature}" are not available for {data_name}. '
                f'Available set_type options: '
                f'{avai_sets} and available protein_feature options: {avai_prots}')
        
        
        
        return avai_sets, avai_prots


class casual_importer():
    
    def __init__(self,delimiter, name, label):
        
        self.delimiter = delimiter
        self.name = name
        self.label = label
        
    def get_data(self,file_name):
        
        """
        Parameters:
            file_name = Name of file holds data. 
                        Format must be specified.
        """
        
        return self_data(file_name = file_name,
                         delimiter = self.delimiter,
                         name = self.name,
                         label = self.label)
    
