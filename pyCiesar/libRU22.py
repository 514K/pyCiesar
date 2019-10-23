def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','х')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ц')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ч')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ш')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','щ')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ъ')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ы')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ь')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','э')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ю')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','я')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','а')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','б')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','в')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','г')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','д')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','е')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ё')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ж')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','з')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','и')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','й')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','к')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','л')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','м')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','н')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','о')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','п')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','р')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','с')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','т')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','у')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ф')+a[k+1:]
    return a