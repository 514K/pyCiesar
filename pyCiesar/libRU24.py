def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ч')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ш')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','щ')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ъ')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ы')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ь')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','э')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ю')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','я')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','а')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','б')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','в')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','г')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','д')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','е')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ё')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ж')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','з')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','и')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','й')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','к')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','л')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','м')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','н')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','о')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','п')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','р')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','с')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','т')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','у')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ф')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','х')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ц')+a[k+1:]
    return a