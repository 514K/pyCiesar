def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','т')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','у')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ф')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','х')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ц')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ч')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ш')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','щ')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ъ')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ы')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ь')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','э')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ю')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','я')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','а')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','б')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','в')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','г')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','д')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','е')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ё')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ж')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','з')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','и')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','й')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','к')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','л')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','м')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','н')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','о')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','п')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','р')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','с')+a[k+1:]
    return a