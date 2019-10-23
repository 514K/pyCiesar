def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','я')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','а')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','б')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','в')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','г')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','д')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','е')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ё')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ж')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','з')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','и')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','й')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','к')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','л')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','м')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','н')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','о')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','п')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','р')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','с')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','т')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','у')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ф')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','х')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ц')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ч')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ш')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','щ')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ъ')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ы')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ь')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','э')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ю')+a[k+1:]
    return a