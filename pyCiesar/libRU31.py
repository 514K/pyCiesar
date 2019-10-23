def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ю')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','я')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','а')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','б')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','в')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','г')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','д')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','е')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ё')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ж')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','з')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','и')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','й')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','к')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','л')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','м')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','н')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','о')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','п')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','р')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','с')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','т')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','у')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ф')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','х')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ц')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ч')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','ш')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','щ')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ъ')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ы')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ь')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','э')+a[k+1:]
    return a