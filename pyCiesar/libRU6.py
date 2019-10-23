def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ё')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ж')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','з')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','и')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','й')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','к')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','л')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','м')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','н')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','о')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','п')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','р')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','с')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','т')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','у')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ф')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','х')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ц')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ч')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ш')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','щ')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ъ')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ы')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ь')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','э')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ю')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','я')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','а')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','б')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','в')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','г')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','д')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','е')+a[k+1:]
    return a