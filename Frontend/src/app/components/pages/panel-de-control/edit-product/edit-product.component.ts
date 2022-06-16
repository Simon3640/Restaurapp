
import { Component, Input, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Category } from '@app/shared/interfaces/category.interface';
import { CategoryService } from '@app/shared/services/category.service';
import { ProductService } from '@app/shared/services/product.service';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-edit-product',
  templateUrl: './edit-product.component.html',
  styleUrls: ['./edit-product.component.scss'],
  
})
export class EditProductComponent implements OnInit {
  product: any = null;
  ing : String[] = [];
  form : FormGroup;
  hideCategory: boolean = false;
  @Input() id: number=0;

  items : String[] = [];

  constructor(
    private route:ActivatedRoute,
    private productSvc:ProductService,
    private categorySvc:CategoryService,
    private modal: NgbActiveModal,
    private fb: FormBuilder
  ) { 
    this.form = this.fb.group({
      checkArray: this.fb.array([]),
    });
  }
  
  
  submitForm() {
    console.log(this.form.value);
  }
  


  ngOnInit(): void {
    this.productSvc.getDetails(this.id).subscribe(
      (res:any) => {
        const result = res;
        this.product = result;
        this.productForm.patchValue(this.product);
      }
    );
    this.getDataFromService();
  
  }

  
  productForm = this.fb.group({
    Name: ['',[Validators.required, Validators.minLength(3), Validators.maxLength(255)]],
    Description: ['',[Validators.required, Validators.minLength(20), Validators.maxLength(300)]],
    Short_Description: ['',[ Validators.minLength(0), Validators.maxLength(100)]],
    Value: [Number, [Validators.required, Validators.min(0), Validators.max(100000000000)]],
    Category: [''],
    Image: ['',[Validators.required]],
    Ingredients: [this.items],
  });


  Entero(Value: number): boolean {
    return Number.isInteger(Value);
  }

  isInvalidForm(controlName: string): boolean {
    return this.productForm.controls[controlName].invalid && this.productForm.controls[controlName].touched;}
  
  onSubmit() {
    console.log(this.productForm.value);
    this.productSvc.updateProduct(this.productForm.value,this.id).subscribe(data => console.log(data));
    this.modal.close('success');
  }

  categories: Category[] = [];
  onAdd(): void {
    console.log(this.productForm.value);
  }


  private getDataFromService(): void {
      this.categorySvc.getCategories().subscribe((res:any) => {
        const results = res;
        this.categories = results
      });
    }
  
    onClose() {
      this.modal.close('closed');
    }
}