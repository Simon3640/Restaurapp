import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Category } from '@app/shared/interfaces/category.interface';
import { CategoryService } from '@app/shared/services/category.service';
import { ProductService } from '@app/shared/services/product.service';


@Component({
  selector: 'app-new-product',
  templateUrl: './new-product.component.html',
  styleUrls: ['./new-product.component.scss']
})
export class NewProductComponent implements OnInit {

  constructor(private productSvc:ProductService ,private fb: FormBuilder, private router:Router, private categorySvc: CategoryService) { }

  productForm = this.fb.group({
    Name: ['',[Validators.required, Validators.minLength(3), Validators.maxLength(255)]],
    Description: ['',[Validators.required, Validators.minLength(20), Validators.maxLength(300)]],
    Short_Description: ['',[ Validators.minLength(0), Validators.maxLength(100)]],
    Value: [Number, [Validators.required, Validators.min(0), Validators.max(100000000000)]],
    Category: ['',[Validators.required]],
    Image: ['',[Validators.required]],
  });

  ngOnInit(): void {
    this.getDataFromService()
  }
  Entero(Value: number): boolean {
    return Number.isInteger(Value);
  }

  isInvalidForm(controlName: string): boolean {
    return this.productForm.controls[controlName].invalid && this.productForm.controls[controlName].touched;}
  
  onSubmit() {
    console.log(this.productForm.value);
    this.productSvc.postProduct(this.productForm.value).subscribe(data => console.log(data));
  }

  categories: Category[] = [];

  private getDataFromService(): void {
      this.categorySvc.getCategories().subscribe((res:any) => {
        const results = res;
        this.categories = results
      });
    }
  
  
}
