export interface Product {
    id: number;
    Name: string;
    Description: string;
    Short_Description: string;
    Value: number;
    Image: string;
    Ingredients: string[];
    Image_Galery?: string[];
}

export interface ProductDTO extends Product, Omit<Product, 'id'> {
    Category : string;
}

export interface PseudoProduct {
    id: number;
    Ingredients: string[];
}