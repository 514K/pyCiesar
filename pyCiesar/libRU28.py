def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ы')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ь')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','э')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ю')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','я')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','а')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','б')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','в')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','г')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','д')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','е')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ё')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ж')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','з')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','и')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','й')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','к')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','л')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','м')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','н')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','о')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','п')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','р')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','с')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','т')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','у')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ф')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','х')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ц')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ч')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ш')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','щ')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ъ')+a[k+1:]
    return a