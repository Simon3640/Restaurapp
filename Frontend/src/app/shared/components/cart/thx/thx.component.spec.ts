import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThxComponent } from './thx.component';

describe('ThxComponent', () => {
  let component: ThxComponent;
  let fixture: ComponentFixture<ThxComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ThxComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ThxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
